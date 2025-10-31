package bci.app.main;

import bci.core.LibraryManager;
import bci.app.exception.FileOpenFailedException;
import bci.core.exception.MissingFileAssociationException;
import bci.core.exception.UnavailableFileException;
import pt.tecnico.uilib.forms.Form;
import pt.tecnico.uilib.menus.Command;
import pt.tecnico.uilib.menus.CommandException;
import java.io.IOException;

class DoOpenFile extends Command<LibraryManager> {
  DoOpenFile(LibraryManager receiver) {
    super(Label.OPEN_FILE, receiver);
  }

  @Override
  protected final void execute() throws CommandException {
    try {
    if (_receiver.isDirty()) {
      if (Form.confirm(Prompt.saveBeforeExit())) {
        if (_receiver.hasAssociatedFile()) {
          _receiver.save();
        } else {
          String saveName = Form.requestString(Prompt.newSaveAs());
          _receiver.saveAs(saveName);
        }
      }
    }
    String fname = Form.requestString(Prompt.openFile());
    _receiver.load(fname);
  } catch (UnavailableFileException | MissingFileAssociationException | IOException e) {
    throw new FileOpenFailedException(e);
  }
  }
}

