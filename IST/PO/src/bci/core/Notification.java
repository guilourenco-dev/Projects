package bci.core;
import java.io.Serializable;

final class Notification implements Serializable {
  private static final long serialVersionUID = 1L;
  private final String _text;
  public Notification(String text) { _text = text; }
  @Override public String toString() { return _text; }
}
