class RoomBooking:

    def quote(self, building: str, floor: int, room: str,
              start_hour: int, end_hour: int,
              projector: bool, sound: bool,
              attendees: int) -> float:

        base = (end_hour - start_hour) * 50.0
        if projector:
            base += 30.0
        if sound:
            base += 20.0
        if attendees > 40:
            base *= 1.15

        if building == "A" and floor >= 3:
            base += 10.0
        if room == "LAB":
            base += 40.0

        return round(base, 2)
