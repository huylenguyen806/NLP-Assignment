from __future__ import absolute_import
import unicodedata
from pyvi import ViPosTagger, ViTokenizer
from models.config import dep_relations, pos_tags, name_to_pos


def nor(sen):
    return unicodedata.normalize('NFC', sen)


def preprocess(sentence):
    sentence = nor(sentence)
    sentence = sentence.replace("bus", "buýt")
    return sentence


def postprocess_pos(pos):
    i = 0
    while i < len(pos):
        if pos[i][0].lower() in ['thời_gian', 'bao lâu']:
            pos[i] = (pos[i][0], 'WH_TIME')
        if pos[i][0].lower() == 'đến':
            pos[i] = (pos[i][0], 'V')
        if pos[i][0].lower() == 'lúc':
            pos[i] = (pos[i][0] + '_' + pos[i+1][0], 'M')
            del pos[i+1]
        i += 1

    return pos


def create_pos(sentence):
    sentence = preprocess(sentence)
    pos = ViPosTagger.postagging(ViTokenizer.tokenize(sentence))
    result = []
    final = []
    for i in range(len(pos[0])):
        result.append((pos[0][i], pos[-1][i]))
    result = postprocess_pos(result)
    i = 0
    while i < len(result):
        if i < len(result) - 2 and pos_tags[result[i][-1]] == pos_tags[result[i+2][-1]] == "numeral" and pos_tags[result[i+1][-1]] == "punctuation":
            temp = (result[i][0] + result[i+1][0] +
                    result[i+2][0], name_to_pos["numeral"])
            i += 3
        else:
            temp = result[i]
            i += 1
        final.append(temp)
    return final


def malt_parser(pos):
    sigma = ["ROOT"]
    beta = pos
    alpha = []

    def shift(_sigma, _beta, _alpha):
        _sigma.append(beta[0])
        del _beta[0]
        return _sigma, _beta, _alpha

    def left_arc(_sigma, _beta, _alpha, rule):
        _alpha.append((rule, beta[0], _sigma[-1]))
        del _sigma[-1]
        return _sigma, _beta, _alpha

    def right_arc(_sigma, _beta, _alpha, rule):
        _alpha.append((rule, _sigma[-1], _beta[0]))
        _sigma.append(beta[0])
        del _beta[0]
        return _sigma, _beta, _alpha

    def reduce(_sigma, _beta, _alpha):
        del _sigma[-1]
        return _sigma, _beta, _alpha

    def get_rule(left, right):
        condition = pos_tags[left[-1]] + "+" + pos_tags[right[-1]]
        try:
            rule = dep_relations[condition]
            return rule
        except Exception:
            return None

    def is_any_rules_of(word, _alpha):
        for rule in _alpha:
            if rule[-1] == word:
                return True
        return False

    while beta:
        word_i = sigma[-1]
        word_j = beta[0]
        rule_right = get_rule(word_i, word_j)
        rule_left = get_rule(word_j, word_i)
        is_any_rule_in_alpha = is_any_rules_of(word_i, alpha)

        if word_i != "ROOT" and not is_any_rule_in_alpha and rule_left:
            sigma, beta, alpha = left_arc(sigma, beta, alpha, rule_left)
            continue
        if rule_right:
            sigma, beta, alpha = right_arc(sigma, beta, alpha, rule_right)
            continue
        if is_any_rule_in_alpha:
            sigma, beta, alpha = reduce(sigma, beta, alpha)
            continue
        sigma, beta, alpha = shift(sigma, beta, alpha)

    return alpha
