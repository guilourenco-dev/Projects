package bci.app.user;

import bci.app.exception.UserRegistrationFailedException;
import bci.core.LibraryManager;
import pt.tecnico.uilib.menus.Command;
import pt.tecnico.uilib.menus.CommandException;
import pt.tecnico.uilib.forms.Form;

class DoRegisterUser extends Command<LibraryManager> {
  private String _name;
  private String _email;
  
  DoRegisterUser(LibraryManager receiver){
    super(Label.REGISTER_USER, receiver);
  }

  @Override
  protected final void execute() throws CommandException {
    _name = Form.requestString(Prompt.userName());
    _email = Form.requestString(Prompt.userEMail());
    if (_name.isEmpty() || _email.isEmpty()){
      throw new UserRegistrationFailedException(_name, _email);
    }
    int id =_receiver.registerUser(_name, _email); 
    if (!_receiver.findUser(id)){
      throw new UserRegistrationFailedException(_name, _email);
    }
    _display.addLine(Message.registrationSuccessful(id));
    _display.display();
  }
}



