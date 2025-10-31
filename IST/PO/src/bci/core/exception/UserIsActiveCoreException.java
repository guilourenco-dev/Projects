package bci.core.exception;

public class UserIsActiveCoreException extends CoreException { // Ou extends Exception
    @java.io.Serial
    private static final long serialVersionUID = 202510221805L;

    public UserIsActiveCoreException(int userId) {
        super("O utente " + userId + " não tem multas para pagar.");

    }
}