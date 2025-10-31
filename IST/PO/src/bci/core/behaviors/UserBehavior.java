package bci.core.behaviors;

import java.io.Serializable;

/**
 * Interface for the State Pattern, representing user behavior.
 * * Defines the contract for state-specific operations, such as
 * determining request limits and calculating loan deadlines,
 * based on the rules in enunciado-3.pdf (Section 1.4).
 */
public interface UserBehavior extends Serializable {

    /**
     * (For Rule 4) Gets the max allowed requests for this behavior.
     */
    int getMaxRequests();

    /**
     * (For Rule 6) Checks if this behavior is 'cumpridor'.
     */
    boolean isCompliant();

    /**
     * (For Deadline) Gets deadline for works with 1 copy.
     */
    int getDeadlineForOneCopy();

    /**
     * (For Deadline) Gets deadline for works with 2-5 copies.
     */
    int getDeadlineForFiveOrLessCopies();

    /**
     * (For Deadline) Gets deadline for works with >5 copies.
     */
    int getDeadlineForMoreThanFiveCopies();

    @Override
    String toString();

}