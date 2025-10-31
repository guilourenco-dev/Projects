package bci.core.behaviors;

/**
 * Concrete State: Represents the "CUMPRIDOR" (compliant) user behavior.
 * Implemented as a Singleton.
 */
public class Cumpridor implements UserBehavior {
    private static final long serialVersionUID = 202510221303L;
    
    /** The single instance of this class. Singleton pattern. */
    private static final Cumpridor INSTANCE = new Cumpridor();

    // Private constructor to prevent outside instantiation. 
    private Cumpridor() {}
    public static Cumpridor getInstance() { return INSTANCE; }
    private Object readResolve() { return INSTANCE; }

    @Override
    public int getMaxRequests() { return 5; }

    @Override
    public boolean isCompliant() { return true; }

    @Override
    public int getDeadlineForOneCopy() { return 8; }

    @Override
    public int getDeadlineForFiveOrLessCopies() { return 15; }

    @Override
    public int getDeadlineForMoreThanFiveCopies() { return 30; }

    @Override
    public String toString() { return "CUMPRIDOR"; }
}