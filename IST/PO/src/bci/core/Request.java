package bci.core;

import java.io.Serializable;

public class Request implements Serializable {

    private static final long serialVersionUID = 202510221200L;

    private final User _user;
    private final Work _work;
    
    /** The deadline, calculated in days from the current date. */
    private int _deadline = 0;

    /**
     * Constructor for a new request.
     * The deadline is set separately by the library after all rules pass.
     *
     * @param user The user making the request.
     * @param work The work being requested.
     */
    public Request(User user, Work work) {
        
        _user = user;
        _work = work;
    }

    public User getUser() {
        return _user;
    }

    public Work getWork() {
        return _work;
    }

    public int getDeadline() {
        return _deadline;
    }

    public void setDeadline(int deadline) {
        _deadline = deadline;
    }
}