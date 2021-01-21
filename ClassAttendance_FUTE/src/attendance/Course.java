package attendance;

import java.util.ArrayList;

public class Course {
	
	private String name;
	
	private String code;
	
	private Instructor instructor;
	
	private ArrayList<CourseSchedule> schedules;
	
	private ArrayList<Student> enrolledStudents;
	
	public Course(String name, String code, Instructor instructor) {
		this.name = name;
		this.code = code;
		this.instructor = instructor;
		
		this.schedules = new ArrayList<>();
		this.enrolledStudents = new ArrayList<>();
	}
	
	public void addSchedule(CourseSchedule schedule) {
		if (!this.schedules.contains(schedule)) {
			this.schedules.add(schedule);
		}
	}
	
	public ArrayList<Student> getEnrolledStudents() {
		return enrolledStudents;
	}
	
	public void setEnrolledStudents(ArrayList<Student> enrolledStudents) {
		this.enrolledStudents = enrolledStudents;
	}
	
	public Instructor getInstructor() {
		return instructor;
	}
	
	public String toString() {
		return String.format("Course: %s", this.name);
	}
}
