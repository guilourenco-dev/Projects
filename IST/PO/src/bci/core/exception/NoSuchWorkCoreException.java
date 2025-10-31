package bci.core.exception;

public class NoSuchWorkCoreException extends CoreException { // Ou extends Exception
    @java.io.Serial
    private static final long serialVersionUID = 202510221802L;

    private final int _workId;

    public NoSuchWorkCoreException(int workId) {
        super("A obra com o identificador " + workId + " não existe.");
        _workId = workId;
    }

    public int getWorkId() {
        return _workId;
    }
}