package bci.core.exception;
public class BorrowingRuleFailedCoreException extends CoreException {
    @java.io.Serial
    private static final long serialVersionUID = 202510221803L;

    public BorrowingRuleFailedCoreException(int userId, int workId, int ruleId) {
        super("A requisição falhou a regra " + ruleId + ".");
    }
}