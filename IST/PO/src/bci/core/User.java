package bci.core;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;
import bci.core.behaviors.UserBehavior;
import bci.core.behaviors.Normal;
import bci.core.behaviors.Cumpridor;
import bci.core.behaviors.Faltoso;
import java.util.ArrayDeque;
import java.util.Deque;


public class User implements Serializable{
    private static final long serialVersionUID = 202508101412L; 
    private final int _id;
    private final String _name;
    private final String _email;
    private boolean _isActive;
    private int _fine;
    private final List<Request> _openRequests;
    private int _onTimeReturnStreak; // Streak of consecutive on-time returns
    private final Deque<Notification> _notifications = new ArrayDeque<>(); 
    private UserBehavior _behavior = Normal.getInstance();
    private final ArrayDeque<Boolean> _lastReturns = new ArrayDeque<>(5);
    

    // Constructor
    public User(int id, String name, String email){
        _id = id;
        _name = name;
        _email = email;
        _isActive = true;
        _fine = 0;
        _openRequests = new ArrayList<>();
        _behavior = Normal.getInstance();
        _onTimeReturnStreak = 0;
    }

    public boolean isActive(){ return _isActive; }
    public int getUserId(){return _id;}
    public String getUserName(){return _name;}
    public int getUserFine(){return _fine;}
    UserBehavior getUserBehavior(){return _behavior;}
    public boolean isCompliant() { return Cumpridor.getInstance() == _behavior; }
    public int getRequestsCount() { return _openRequests.size(); }
    public int getMaxRequests(){ return _behavior.getMaxRequests(); }
   

    void setUserBehavior(UserBehavior behavior){ _behavior = behavior; }
    void setActive(boolean isActive) { _isActive = isActive; }
    


    public void addRequest(Request newRequest) { _openRequests.add(newRequest); }

    Request findOpenRequest(Work work) {
        for (Request req : _openRequests) {
            if (req.getWork().equals(work)) {
                return req;
            }
        }
        return null;
    }

    void removeRequest(Request request) { _openRequests.remove(request); }

    void addFine(int amount) { _fine = amount;}

    public void checkBehaviorUpdateOnReturn() {
        // A late return will have already set behavior to Faltoso.
        // This method only handles on-time returns.
        if (_behavior.equals(Faltoso.getInstance())) {  // A single on-time return promotes Faltoso -> Normal
            
            this.setUserBehavior(Normal.getInstance());
            _onTimeReturnStreak = 1; // Start a new streak
            
        } else if (_behavior.equals(Normal.getInstance())) {
            
            _onTimeReturnStreak++;  // Increment the streak for a Normal user
            if (_onTimeReturnStreak >= 5) {  // 5 on-time returns in a row promotes Normal -> Cumpridor
                this.setUserBehavior(Cumpridor.getInstance());
            }
        }
    }

    public void resetOnTimeStreak() { _onTimeReturnStreak = 0; } 

    void clearFine() {
        _fine = 0;
    }

    public boolean hasOpenRequest(Work work) { return findOpenRequest(work) != null; }

    /**
     * Returns a string describing the user.
     * If the user is active, the string is in the format:
     * "id - name - email - behavior - ACTIVO"
     * If the user is suspended, the string is in the format:
     * "id - name - email - behavior - SUSPENSO - EUR fine"
     * @return a string describing the user
     */
    String getDescription() {
        if (_isActive) {     
            return String.format("%d - %s - %s - %s - ACTIVO", _id, _name, 
            _email, _behavior.toString());
        } else if (!_isActive) {
            return String.format("%d - %s - %s - %s - SUSPENSO - EUR %d", _id, 
            _name, _email, _behavior.toString(), _fine);
        }
        return null;
    }

    void addNotification(Notification n) { _notifications.addLast(n); }

    List<Notification> consumeNotifications() {
    var out = new ArrayList<>(_notifications);
    _notifications.clear();
    return out;
}
    
   

void recordReturn(boolean onTime){
  _lastReturns.addLast(onTime);
  if (_lastReturns.size() > 5) _lastReturns.removeFirst();

  // 5 pontuais seguidas → CUMPRIDOR
  if (_lastReturns.size()==5 && _lastReturns.stream().allMatch(Boolean::booleanValue)) {
    setUserBehavior(Cumpridor.getInstance());
    return;
  }

  int num = _lastReturns.size();
  if (num >= 3){
    var it = _lastReturns.iterator(); 
    boolean[] vet = new boolean[num]; 
    int i=0; 
    while(it.hasNext()) { vet[i++] = it.next(); }
    // 3 atrasos seguidos → FALTOSO
    if (!vet[num - 1] && !vet[num - 2] && !vet[num - 3]) { setUserBehavior(Faltoso.getInstance()); return; }
    // Faltoso + 3 pontuais seguidas → NORMAL
    if (getUserBehavior()==Faltoso.getInstance() && vet[num - 1] && vet[num - 2] && vet[num - 3]) {
      setUserBehavior(Normal.getInstance());
      return;
    }
  }

  // um atraso quebra CUMPRIDOR → NORMAL
  if (!onTime && getUserBehavior()==Cumpridor.getInstance()) setUserBehavior(Normal.getInstance());
}


public UserBehavior behavior(){ return _behavior; }

public boolean hasOverdue(int currentDate) {
  for (Request r : _openRequests) {
    if (r.getDeadline() < currentDate) return true;
  }
  return false;
}


public int getTotalRequestedValue() {
        int totalValue = 0;
        
        for (Request req : _openRequests) {
            
            Work work = req.getWork(); 
            totalValue += work.getPrice(); 
        }
        return totalValue;
    }
}

