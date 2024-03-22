from copy import deepcopy
from visitor import *


# Unit Clause = 1 Variable
def unit_clause(node: NodeClause):
    return len(node.vars) == 1


# Does a Clause contain the complement of any variable?
def has_negative(node: NodeClause):
    for var in node.vars:
        if var.neg:
            return True
    return False


# Determine all the variable names present in the Formula
def all_vars(node: NodeFormula):
    formula_vars = []
    for clause in node.clauses:
        for var in clause.vars:
            if var.identifier not in formula_vars:
                formula_vars.append(var.identifier)
    return formula_vars


# Does each Clause contain a complement?
# If so, the Formula has a solution!
def negative_in_each_clause(node: NodeFormula):
    for clause in node.clauses:
        if not has_negative(clause):
            return False
    return True


# If we assign a Variable from a Unit Clause, we will have to delete its complement in other Clauses (if present).
# In case this makes another Clause empty, we know there is no solution.
def delete_var_from_clause(node: NodeClause, var: NodeVar):
    # Start with an empty list, all other vars will be added to it.
    remaining_vars = []
    for clause_var in node.vars:
        # If a Variable is the complement of the given Variable: do not add.
        if clause_var.identifier == var.identifier and clause_var.neg != var.neg:
            continue
        # Add otherwise.
        else:
            remaining_vars.append(clause_var)
    # Update the Variables of the Node.
    node.vars = remaining_vars
    # We return whether the resulting Clause is empty, empty = Formula not satisfiable!
    return len(remaining_vars) != 0


# This function returns all Clauses in a Formula that aren't the given Clause.
# Necessary for Variable deletion.
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
        pass

    def visitNodeClause(self, node: NodeClause):
        pass

    def visitNodeFormula(self, node: NodeFormula):
        node_copy = deepcopy(node)
        # We must know all Variable names to assign.
        all_variables = all_vars(node_copy)
        assignment = {}
        # Initially, set all Variables to False.
        for var in all_variables:
            assignment[var] = False
        # The problematic Clauses are the Unit Clauses with a positive Variable.
        # As long as they are present, we will need to assign these Variables and alter the Formula.
        while not negative_in_each_clause(node_copy):
            to_be_deleted = None
            for clause in node_copy.clauses:
                if unit_clause(clause):
                    # Keep track of this Variable for deletion in other Clauses later.
                    to_be_deleted = clause.vars[0]
                    # We know which value the Variable must have.
                    assignment[to_be_deleted.identifier] = not clause.vars[0].neg
                    # Remove the Unit Clause from the formula.
                    node_copy.clauses = get_formula_without_given_clause(node_copy, clause)
                    # For safety: only delete at most 1 Unit Clause per iteration.
                    break
            # If to_be_deleted is not None, it implies a Unit Clause was found and a Variable must be deleted.
            if to_be_deleted:
                for clause in node_copy.clauses:
                    if not delete_var_from_clause(clause, to_be_deleted):
                        return "No truth assignment found!"
        return assignment
