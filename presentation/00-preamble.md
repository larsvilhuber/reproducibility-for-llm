```{r}

# Define a function to read and truncate lines, with a prefix
mylines <- function(inputfile, charlimit = 45, prefix = "") {
    file_content <- readLines(inputfile)
    # Truncate each line to x characters
    truncated_content <- substr(file_content, 1, charlimit)
    # Prepend the prefix to each line
    prefixed_content <- paste0(prefix, truncated_content)
    # Display the content verbatim
    cat(prefixed_content, sep = "\n")
}

mylinesverb <- function(inputfile) {
    text <- readLines(inputfile)

    # Initialize variables
    chunks <- list()
    current_chunk <- character(0)

    # Process each line
    for (line in text) {
    if (nchar(line) == 0 && length(current_chunk) > 0) {
        # Empty line marks chunk boundary if we have content
        chunks[[length(chunks) + 1]] <- current_chunk
        current_chunk <- character(0)
    } else if (nchar(line) > 0) {
        # Add non-empty lines to current chunk
        current_chunk <- c(current_chunk, line)
    }
    }

    # Add final chunk if not empty
    if (length(current_chunk) > 0) {
        chunks[[length(chunks) + 1]] <- current_chunk
    }

    # Write out chunks as Markdown code blocks
    for (i in seq_along(chunks)) {
        cat("````\n")
        cat(paste(chunks[[i]], collapse="\n"))
        cat("\n````\n")
        if (i < length(chunks)) {
            cat("\n---\n\n")
        }
    }
}


```