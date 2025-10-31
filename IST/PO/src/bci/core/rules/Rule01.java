package bci.core.rules;

import bci.core.User;
import bci.core.Work;

/**
 * Rule 1: User cannot request the same work twice (if already open).
 */
public class Rule01 extends Rule {
    public Rule01() {
        super(1);
    }

    /**
     * Checks if the user has an open request for the given work.
     * 
     * @param work The work being requested.
     * @param user The user making the request.
     * @return true if the user does not have an open request for the given work, false otherwise.
     */
    @Override
    public boolean check(Work work, User user) {
        return !user.hasOpenRequest(work);
    }
}