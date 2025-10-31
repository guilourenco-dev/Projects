package bci.core.rules;

import java.io.Serializable;
import bci.core.User;
import bci.core.Work;

/**
 * Represents the abstract "Strategy" for a request validation rule.
 * Implements Comparable to allow sorting by ID. 
 */
public abstract class Rule implements Serializable, Comparable<Rule> {

    private static final long serialVersionUID = 202510221207L;

    private final int _id;

    /**
     * Constructor for a rule.
     * @param id The rule's numeric identifier. 
     */
    public Rule(int id) {
        _id = id;
    }

    /**
     * @return The identifier of this rule.
     */
    public int getId() {
        return _id;
    }

    /**
     * The core strategy method. Checks if a given user and work
     * comply with this specific rule.
     *
     * @param work The work being requested.
     * @param user The user making the request.
     * @return true if the rule passes, false otherwise.
     */
    public abstract boolean check(Work work, User user);

    /**
     * Allows sorting rules by their ID in ascending order. 
     */
    @Override
    public int compareTo(Rule other) {
        return Integer.compare(this._id, other._id);
    }
}