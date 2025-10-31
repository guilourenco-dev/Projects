package bci.core.rules;

import bci.core.User;
import bci.core.Work;

/**
 * Rule 3: The work must have at least one copy available.
 */
public class Rule03 extends Rule {
    public Rule03() {
        super(3);
    }

    /**
     * Checks if the given work has at least one copy available.
     * 
     * @param work The work being requested.
     * @param user The user making the request.
     * @return true if the work has at least one copy available, false otherwise.
     */
    @Override
    public boolean check(Work work, User user) {
        return work.getAvailableCopies() > 0;
    }
}