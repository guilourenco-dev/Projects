package bci.app.main;

import bci.core.LibraryManager;
import bci.app.exception.FileOpenFailedException;
import bci.core.exception.MissingFileAssociationException;  
import pt.tecnico.uilib.menus.Command;
import pt.tecnico.uilib.forms.Form;
import java.io.IOException;

class DoSaveFile extends Command<LibraryManager> {
  DoSaveFile(LibraryManager r) { super(Label.SAVE_FILE, r); }

  @Override
  protected final void execute() throws FileOpenFailedException {
   /**try {
      if (_receiver.hasAssociatedFile()) _receiver.save();
    else _receiver.saveAs(Form.requestString(Prompt.newSaveAs()));
  } catch (MissingFileAssociationException | java.io.IOException e) {
    throw new bci.app.exception.FileOpenFailedException(e);
  }
  **/
  try {
    if (_receiver.hasAssociatedFile()) {
      _receiver.save();
    } else {
      String saveName = Form.requestString(Prompt.newSaveAs());
      _receiver.saveAs(saveName);
    }
    _receiver.setDirty(false);
  } catch (MissingFileAssociationException | IOException e) {
    throw new FileOpenFailedException(e);
  }
  }
}
