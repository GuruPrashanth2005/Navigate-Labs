attendance = eval(input("Attendance (list of tuples): "))
session_count = {}
for session, attendee in attendance:
    session_count[session] = session_count.get(session, 0) + 1
attendee_count = {}
for session, attendee in attendance:
    attendee_count[attendee] = attendee_count.get(attendee, 0) + 1
multi_session = [a for a, c in attendee_count.items() if c > 1]
print(f"Attendees per session: {session_count}")
print(f"Multi-session attendees: {multi_session if multi_session else 'None'}")