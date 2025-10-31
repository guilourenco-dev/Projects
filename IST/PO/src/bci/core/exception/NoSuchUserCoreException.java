package bci.core.exception;

public class NoSuchUserCoreException extends CoreException { 
    @java.io.Serial
    private static final long serialVersionUID = 202510221801L;

    private final int _userId;

    public NoSuchUserCoreException(int userId) {
        super("O utente com o identificador " + userId + " não existe.");
        _userId = userId;
    }

    public int getUserId() {
        return _userId;
    }
}