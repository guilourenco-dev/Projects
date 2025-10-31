package bci.core.rules;

import bci.core.User;
import bci.core.Work;

/**
 * Rule 5: The work's category cannot be 'REFERENCE'. 
 */
public class Rule05 extends Rule {
    public Rule05() {
        super(5);
    }

    /**
     * Checks if the given work is not a reference work.
     * 
     * @param work The work being requested.
     * @param user The user making the request.
     * @return true if the work is not a reference work, false otherwise.
     */
    @Override
    public boolean check(Work work, User user) {
        return !work.isReference();
    }
}