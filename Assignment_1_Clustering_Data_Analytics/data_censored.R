library(TrialEmulation)

# Load the dataset
data("data_censored")

# Define the output file path (adjust as needed)
output_file <- "data_censored.csv"  # Saves in the current working directory

# Export to CSV
write.csv(data_censored, output_file, row.names = FALSE)

# Print success message
cat("Dataset successfully exported to", output_file, "\n")

# Optional: Print first few rows to verify
head(data_censored)