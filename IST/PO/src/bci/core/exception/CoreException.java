package bci.core.exception;

public abstract class CoreException extends Exception {
    @java.io.Serial
    private static final long serialVersionUID = 202510221800L;

    public CoreException() {
        super();
    }

    public CoreException(String message) {
        super(message);
    }

    public CoreException(String message, Throwable cause) {
        super(message, cause);
    }
}