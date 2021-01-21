package attendance;

import java.util.ArrayList;
import java.util.Date;

public class CourseSchedule {
	
	private Course course;
	
	private Date date;
	
	private String location;
	
	private ArrayList<Student> students; // students who were present for the course
	
	public CourseSchedule(Course course, Date date, String location) {
		this.course = course;
		this.date = date;
		this.location = location;
		this.students = new ArrayList<>();
	}
	
	public ArrayList<Student> getStudents() {
		return students;
	}
	
	public void addStudent(Student student) {
		this.students.add(student);
	}
	
	public boolean attended(Student student) {
		return this.students.contains(student);
	}
	
	public void generateReport() {
		System.out.println("===============Attendance Report====================");
		System.out.println("Course: " + this.course);
		System.out.println("Date: " + this.date.toString());
		System.out.println("Instructor: " + this.course.getInstructor().getName());
		System.out.println("Location: " + this.location);
		System.out.println("====================================================");
		
		int count = 0;
		for (Student student : this.course.getEnrolledStudents()) {
			System.out.printf("%d \t\t %s \t\t %s\n", ++count, student.getName(),
					this.attended(student) ? "PRESENT" : "ABSENT");
		}
	}
	
	@Override
	public String toString() {
		return "CourseSchedule{" +
				"course=" + course +
				", date=" + date +
				", location='" + location + '\'' +
				'}';
	}
}
