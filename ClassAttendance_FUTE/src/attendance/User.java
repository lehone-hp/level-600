package attendance;

public class User {
	
	private String name;
	
	private String username;
	
	private String email;
	
	private String password;
	
	public User(String name) {
		this.name = name;
	}
	
	public User(String name, String username, String email, String password) {
		this.name = name;
		this.username = username;
		this.email = email;
		this.password = password;
	}
	
	public String getName() {
		return name;
	}
	
	public void setName(String name) {
		this.name = name;
	}
	
	public void login(String username, String password) {
	
	}
	
	public String toString() {
		return String.format("%s", this.name);
	}
}
