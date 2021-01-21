package attendance;

public class Instructor extends User {
	
	private String faculty;
	
	private String phone;
	
	public Instructor(String name) {
		super(name);
	}
	
	public void takeAttendance(Student student, CourseSchedule schedule) {
		if (schedule != null) {
			if (!schedule.getStudents().contains(student)) {
				schedule.addStudent(student);
			} else {
				System.out.printf("Attendance for %s has already been recorded", student.getName());
			}
		}
	}
	
	public String getFaculty() {
		return faculty;
	}
	
	public void setFaculty(String faculty) {
		this.faculty = faculty;
	}
	
	public String getPhone() {
		return phone;
	}
	
	public void setPhone(String phone) {
		this.phone = phone;
	}
	
	public String toString() {
		return String.format("Instructor: %s", this.getName());
	}
}
