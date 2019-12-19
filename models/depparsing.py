from __future__ import absolute_import
from pyvi import ViPosTagger, ViTokenizer
from models.config import dep_relations, pos_tags


def create_pos(sentence):
    pos = ViPosTagger.postagging(ViTokenizer.tokenize(sentence))
    result = []
    for i in range(len(pos[0])):
        result.append((pos[0][i], pos[-1][i]))
    return result


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
        rule_left = get_rule(word_j, word_i)
        rule_right = get_rule(word_i, word_j)
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
