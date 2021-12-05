########################################
################ Part 1 ################
########################################

sample_course <- strsplit(readLines("sample_course.txt"), "\\s")

input <- strsplit(readLines("input.txt"), "\\s")

follow_course <- function(x) {
  dirs <- vapply(x, `[[`, character(1), 1)
  mags <- as.integer(vapply(x, `[[`, character(1), 2))
  
  forwards <- grep("^f", dirs)
  ups <- grep("^u", dirs)
  downs <- grep("^d", dirs)
  
  horiz <- sum(mags[forwards])
  depth <- sum(mags[downs]) - sum(mags[ups])
  return(horiz * depth)
}

follow_course(input)

########################################
################ Part 2 ################
########################################

follow_aim_course <- function(x) {
    dirs <- vapply(x, `[[`, character(1), 1)
    mags <- as.integer(vapply(x, `[[`, character(1), 2))
    
    forwards <- grep("^f", dirs)
    
    aim <- cumsum(ifelse(grepl("^d", dirs), mags, 0) - 
                  ifelse(grepl("^u", dirs), mags, 0))
    
    horiz <- sum(mags[forwards])
    depth <- sum(ifelse(grepl("^f", dirs), mags * aim, 0))
    return(horiz * depth)
}

follow_aim_course(input)
