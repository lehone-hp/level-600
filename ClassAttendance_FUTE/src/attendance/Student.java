package attendance;

import java.util.Date;

public class Student extends User {
	
	private String matricule;
	
	private Date dob;
	
	public Student(String name) {
		super(name);
	}
	
	public String toString() {
		return String.format("Student: %s", this.getName());
	}
}
