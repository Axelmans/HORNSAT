from copy import deepcopy
from visitor import *


def unit_clause(node: NodeClause):
    return len(node.vars) == 1


def has_negative(node: NodeClause):
    for var in node.vars:
        if var.neg:
            return True
    return False


def all_vars(node: NodeFormula):
    formula_vars = []
    for clause in node.clauses:
        for var in clause.vars:
            if var.identifier not in formula_vars:
                formula_vars.append(var.identifier)
    return formula_vars


def negative_in_each_clause(node: NodeFormula):
    for clause in node.clauses:
        if not has_negative(clause):
            return False
    return True


def delete_var_from_clause(node: NodeClause, var: NodeVar):
    remaining_vars = []
    for clause_var in node.vars:
        if clause_var.identifier == var.identifier and clause_var.neg != var.neg:
            continue
        else:
            remaining_vars.append(clause_var)
    node.vars = remaining_vars
    return len(remaining_vars) != 0


def get_formula_without_given_clause(node: NodeFormula, clause: NodeClause):
    if clause not in node.clauses:
        return
    else:
        other_clauses = []
        for formula_clause in node.clauses:
            if formula_clause != clause:
                other_clauses.append(formula_clause)
        return other_clauses


class HornSolver(Visitor):

    def visitNodeVar(self, node: NodeVar):
        return not node.neg

    def visitNodeClause(self, node: NodeClause):
        return node.vars[0], node.vars[0].accept(self)

    def visitNodeFormula(self, node: NodeFormula):
        node_copy = deepcopy(node)
        all_variables = all_vars(node_copy)
        assignment = {}
        for var in all_variables:
            assignment[var] = False
        while not negative_in_each_clause(node_copy):
            to_be_deleted = None
            for clause in node_copy.clauses:
                if unit_clause(clause):
                    to_be_deleted = clause.vars[0]
                    assignment[to_be_deleted.identifier] = not clause.vars[0].neg
                    node_copy.clauses = get_formula_without_given_clause(node_copy, clause)
                    break
            if to_be_deleted:
                for clause in node_copy.clauses:
                    if not delete_var_from_clause(clause, to_be_deleted):
                        return "No truth assignment found!"
        return assignment
