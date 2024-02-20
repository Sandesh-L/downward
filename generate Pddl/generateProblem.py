def parse_input_file(file_path):
    notes_locations = []
    with open(file_path, 'r') as file:
        for line in file:
            # Skip empty lines or lines not starting with "note"
            if not line.strip().startswith("note"):
                continue
            
            parts = line.strip().split()
            # Check if parts have at least a note name following "note"
            if len(parts) < 2:
                print(f"Skipping incomplete line: {line.strip()}")
                continue

            note = parts[1]
            locations_str = parts[2:]  # Get the location strings

            locations = []
            for loc_str in locations_str:
                try:
                    string, fret = loc_str.split(',')
                    locations.append((int(string), int(fret)))
                except ValueError:
                    # Skip any parts that cannot be correctly parsed
                    print(f"Skipping malformed location entry: {loc_str} in line: {line.strip()}")
                    continue

            if locations:  # Only add notes with valid locations
                notes_locations.append((note, locations))

    return notes_locations


def generate_pddl_problem(notes_locations, problem_name="music_piece", domain_name="guitar_fretboard", output_file="problem.pddl"):
    notes = set(note for note, _ in notes_locations)
    locations = set(f"loc{string}_{fret}" for _, locs in notes_locations for string, fret in locs)
    matches = [f"(matches loc{string}_{fret} {note})" for note, locs in notes_locations for string, fret in locs]

    notes_str = " ".join(sorted(notes))
    locations_str = " ".join(sorted(locations))
    matches_str = "\n    ".join(sorted(matches))

    problem_pddl = f"""(define (problem {problem_name})
  (:domain {domain_name})
  (:objects
    {notes_str} - note
    {locations_str} - location
  )
  (:init
    {matches_str}
  )
  (:goal
    (and
      {" ".join(f"(note-placed {note})" for note in notes)}
    )
  )
)
"""
    with open(output_file, "w") as file:
        file.write(problem_pddl)
    print(f"Problem PDDL file '{output_file}' generated.")

def main(input_file_path):
    notes_locations = parse_input_file(input_file_path)
    generate_pddl_problem(notes_locations)

if __name__ == "__main__":
    input_file_path = "./input.txt"  # Change to your actual input file path
    main(input_file_path)
