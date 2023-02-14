# Read a file with number of steps taken for each day of the year.
# Calculate the average number of steps taken.
# Includes exception handlers for various error conditions that could occur.
def main():
    filename = 'step.txt'
    try:
        steps_file = open(filename, 'r')  # Open the file

        total_steps = 0      # Initialize counters
        line_count = 0

        for line in steps_file:    # Read each record (line) in the file
            total_steps = total_steps + int(line)
            line_count = line_count + 1
        steps_file.close()  # Close the file
    except OSError as err:
        print('Error: cannot access file,', filename)
        print('Error:', err)
    except FileNotFoundError as err:
        print('Error: cannot find file,', filename)
        print('Error:', err)
    except ValueError as err:
        print('Error: invalid data found in file', filename)
        print('Error:', err)
    except Exception as err:  # catch-all error handler, if the above handlers do not apply
        print('An unknown error occurred')
        print('Error:', err)

    # Calculate the average and display
    average = total_steps / line_count
    print('The average number of steps taken in',
          line_count, 'days was', format(average, ',.1f'))


main()