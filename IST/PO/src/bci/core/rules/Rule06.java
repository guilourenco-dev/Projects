package bci.core.rules;

import bci.core.User;
import bci.core.Work;


public class Rule06 extends Rule {
    public Rule06() {
        super(6);
    }

    /**
     * Checks if the user is compliant or if the work price is less than or equal to 25.
     * 
     * @param work the work being requested
     * @param user the user making the request
     * @return true if the user is compliant or if the work price is less than or equal to 25, false otherwise
     */
    @Override
    public boolean check(Work work, User user) {
        return user.isCompliant() || work.getPrice() <= 25;
    }
}