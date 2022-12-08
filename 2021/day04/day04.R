########################################
################ Part 1 ################
########################################

library(tidyverse)

get_game <- function(path) {
  raw <- readLines(path)
  game_sequence <- as.numeric(str_split(raw[[1]], ",")[[1]])
  
  boards_raw <- raw[3:length(raw)]
  empty_row_idxs <- which(boards_raw=="")
  board_size <- empty_row_idxs[[1]]-1
  boards_raw <- boards_raw[-empty_row_idxs]
  boards <- split(boards_raw, ceiling(seq_along(boards_raw) / board_size))
  
  boards <- boards %>%
    # within each board, trim the lines
    map(map_chr, str_trim) %>%
    # split row chars into vectors of cells
    map(str_split, "\\s+") %>%
    # make ints
    map(map, as.numeric) %>%
    # convert to matrices
    map(~ do.call(rbind, .))
  
  return(list(numbers = game_sequence,
              boards = boards,
              mark_sheets = rep(list(matrix(rep(FALSE, board_size ^ 2), board_size)), length(boards))))
  
}

mark <- function(board, mark_sheet = NULL, number = NULL) {
  if (is.null(mark_sheet)) mark_sheet <- matrix(rep(FALSE, length(board)), nrow(board), nrow(board))
  # initialize sheet
  if (is.null(number)) return(mark_sheet)
  return(mark_sheet | (board==number))
}

# a winner has a full row or column of trues

check_winner <- function(mark_sheet) {
  board_size <- nrow(mark_sheet)
  for (i in 1:board_size) {
    # row
    if (all(mark_sheet[i,]) | all(mark_sheet[,i])) return(TRUE)
  }
  return(FALSE)
}

print_game <- function(boards, mark_sheets) {
  for (i in 1:length(boards)) {
    print(boards[[i]] * mark_sheets[[i]])
  }
}

run_game <- function(game, debug = FALSE) {
  winners <- rep(FALSE, length(game$boards))
  i <- 0
  while (!any(winners)) {
    i <- i + 1
    if (debug) cat(game$numbers[[i]], fill = TRUE)
    game$mark_sheets <- map2(game$boards, game$mark_sheets, mark, number = game$numbers[[i]])
    winners <- map_lgl(game$mark_sheets, check_winner)
  }
  winner <- which(winners)
  score <- sum(game$boards[[winner]] * !game$mark_sheets[[winner]]) * game$numbers[[i]]
  # once here, there is a winner
  cat("Player", winner, "wins!", fill = TRUE)
  cat("Score:", score, fill = TRUE)
  invisible(score)
}

sample_game <- get_game("sample_input.txt")
game <- get_game("input.txt")

run_game(sample_game)
run_game(game)


########################################
################ Part 2 ################
########################################

run_game2 <- function(game, debug = FALSE) {
  player_idxs <- seq_along(game$boards)
  winners <- rep(FALSE, length(game$boards))
  i <- 0
  # run while still multiple players or the single player
  # still hasn't won
  while (length(winners) > 1 | !any(winners)) {
    i <- i + 1
    if (debug) cat(game$numbers[[i]], fill = TRUE)
    game$mark_sheets <- map2(game$boards, game$mark_sheets, mark, number = game$numbers[[i]])
    winners <- map_lgl(game$mark_sheets, check_winner)
    if (debug & any(winners)) cat("Winners:", which(winners), fill = TRUE)
    # update player list if still multiple players (winners > 1) & there is a new winner
    if (length(winners) > 1 & any(winners)) {
      # UPDATE PLAYER LIST
      winner_idxs <- which(winners)
      game$boards <- game$boards[-winner_idxs]
      game$mark_sheets <- game$mark_sheets[-winner_idxs]
      winners <- winners[-winner_idxs]
      player_idxs <- player_idxs[-winner_idxs]
    }
  }
  winner <- which(winners)
  winner_orig_idx <- player_idxs[[winner]]
  score <- sum(game$boards[[winner]] * !game$mark_sheets[[winner]]) * game$numbers[[i]]
  # once here, there is a winner
  cat("Player", winner_orig_idx, "is the last winner.", fill = TRUE)
  cat("Score:", score, fill = TRUE)
  invisible(score)
}

sample_game <- get_game("sample_input.txt")
game <- get_game("input.txt")

run_game2(sample_game)
run_game2(game)
