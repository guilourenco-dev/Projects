package bci.app.work;

import bci.core.LibraryManager;
import pt.tecnico.uilib.menus.Command;
import pt.tecnico.uilib.forms.Form;


class DoPerformSearch extends Command<LibraryManager> {

  DoPerformSearch(LibraryManager receiver) {
    super(Label.PERFORM_SEARCH, receiver);
  }

  @Override
  protected void execute() {
    String term = Form.requestString(Prompt.searchTerm()); 
    for (String line : _receiver.searchWorks(term))
      _display.addLine(line);
    _display.display();
  }
}
