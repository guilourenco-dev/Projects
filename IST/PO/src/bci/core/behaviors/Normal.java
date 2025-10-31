package bci.core.behaviors;

/**
 * Concrete State: Represents the "NORMAL" user behavior.
 * Implemented as a Singleton.
 */
public class Normal implements UserBehavior {
    private static final long serialVersionUID = 202510221301L;
    
    /** The single instance of this class. Singleton pattern. */
    private static final Normal INSTANCE = new Normal();

    /** Private constructor to prevent outside instantiation. */
    private Normal() {}
    public static Normal getInstance() { return INSTANCE; }
    private Object readResolve(){ return INSTANCE; }

    @Override
    public int getMaxRequests() { return 3; }

    @Override
    public boolean isCompliant() { return false; }

    @Override
    public int getDeadlineForOneCopy() { return 3; }

    @Override
    public int getDeadlineForFiveOrLessCopies() { return 8; }

    @Override
    public int getDeadlineForMoreThanFiveCopies() { return 15; }

    @Override
    public String toString() { return "NORMAL"; }
}