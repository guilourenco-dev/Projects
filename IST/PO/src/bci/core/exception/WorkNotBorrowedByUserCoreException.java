package bci.core.exception;

public class WorkNotBorrowedByUserCoreException extends CoreException { // Ou extends Exception
    @java.io.Serial
    private static final long serialVersionUID = 202510221804L;

    public WorkNotBorrowedByUserCoreException(int workId, int userId) {
        super("A obra " + workId + " não foi requisitada pelo utente " + userId + ".");
    }
}