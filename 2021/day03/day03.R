########################################
################ Part 1 ################
########################################

sample_binary <- strsplit(readLines("sample_binary.txt"), "")

input <- strsplit(readLines("input.txt"), "")

get_power_consumption <- function(x) {
  record_length = length(x[[1]])
  nobs <- length(x)
  
  gamma <- 0
  epsilon <- 0
  
  for (i in 1:record_length) {
    bit_vec <- sort(as.integer(vapply(x, `[[`, character(1), i)))
    if ((nobs %% 2) != 0) {
      mcb_gamma <- bit_vec[ceiling(nobs / 2)]
    } else {
      # No guidance on ties; assume doesn't happen.
      mcb_gamma <- bit_vec[nobs / 2]
    }
    
    # by definition
    mcb_epsilon <- as.integer(!mcb_gamma)
    
    gamma <- gamma + mcb_gamma * 2 ^ (record_length - i)
    epsilon <- epsilon + mcb_epsilon * 2 ^ (record_length - i)
  }
  
  cat(gamma, epsilon, fill = TRUE)
  return(gamma * epsilon)
}

get_power_consumption(input)
# [1] 4139586

########################################
################ Part 2 ################
########################################

apply_bit_criteria <- function(vec, rating) {
  vec <- sort(vec)
  nobs <- length(vec)
  
  if ((nobs %% 2) != 0) {
    mcb <- vec[ceiling(nobs / 2)]
  } else {
    middle <- vec[(nobs / 2) + c(0, 1)]
    if (sum(middle) == 1) {
      # start with oxygen's rule for this case; will reverse later for co2
      mcb <- 1
    } else {
      mcb <- middle[1]
    }
  }
  
  return(switch(rating,
                "oxygen" = mcb,
                "co2" = as.integer(!mcb)))
}

narrow_binary <- function(x, rating) {
  bit <- 1
  while (length(x) != 1) {
    bit_vec <- as.integer(vapply(x, `[[`, character(1), bit))
    mcb <- apply_bit_criteria(bit_vec, rating)
    x <- x[bit_vec == mcb]
    bit <- bit + 1
  }
  return(x[[1]])
}

convert_binary <- function(x) {
  len <- length(x)
  res <- 0
  for (i in seq_along(x)) {
    res <- res + as.integer(x[i]) * (2 ^ (len - i))
  }
  return(res)
}

get_life_rating <- function(x) {
  oxygen <- convert_binary(narrow_binary(x, "oxygen"))
  c02 <- convert_binary(narrow_binary(x, "co2"))
  cat(oxygen, c02, fill = TRUE)
  return(oxygen * c02)
}

get_life_rating(input)
# [1] 1800151