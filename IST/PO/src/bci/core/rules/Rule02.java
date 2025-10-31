package bci.core.rules;

import bci.core.User;
import bci.core.Work;

public class Rule02 extends Rule {
    public Rule02() {
        super(2);
    }

    /**
     * Checks if the user is active.
     * 
     * @param work The work being requested.
     * @param user The user making the request.
     * @return true if the user is active, false otherwise.
     */
    @Override
    public boolean check(Work work, User user) {
        return user.isActive();
    }
}