package bci.core.behaviors;


/**
 * Concrete State: Represents the "FALTOSO" (defaulting) user behavior.
 * Implemented as a Singleton.
 */
public class Faltoso implements UserBehavior {
    private static final long serialVersionUID = 202510221302L;
    
    /** The single instance of this class. Singleton pattern. */
    private static final Faltoso INSTANCE = new Faltoso();

    /** Private constructor to prevent outside instantiation. */
    private Faltoso() {}
    public static Faltoso getInstance() { return INSTANCE; }
    private Object readResolve() { return INSTANCE; }

    @Override
    public int getMaxRequests() { return 1; } 

    @Override
    public boolean isCompliant() { return false; }

    @Override
    public int getDeadlineForOneCopy() { return 2; }

    @Override
    public int getDeadlineForFiveOrLessCopies() { return 2; }

    @Override
    public int getDeadlineForMoreThanFiveCopies() { return 2; }

    @Override
    public String toString() { return "FALTOSO"; }
}