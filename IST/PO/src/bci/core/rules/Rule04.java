package bci.core.rules;

import bci.core.User;
import bci.core.Work;

/**
 * Rule 4: User must not be over their personal request limit.
 */
public class Rule04 extends Rule {
    public Rule04() {
        super(4);
    }

    /**
     * Checks if the user is compliant with their personal request limit.
     * 
     * @param work The work being requested.
     * @param user The user making the request.
     * @return true if the user has not exceeded their personal request limit, false otherwise.
     */
    @Override
    public boolean check(Work work, User user) {
        return user.getRequestsCount() < user.getMaxRequests();
    }
}