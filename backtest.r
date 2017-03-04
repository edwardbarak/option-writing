delta <- function(df, df_row) {
  type <- tolower(df[df_row, 'Type'])
  underlying <- df[df_row, 'ParentClose']
  strike <- df[df_row, 'strike']
  dividendYield <- 0.004609833
  riskFreeRate <- 0.0053
  maturity <- calc_maturity(df, df_row)
  
}

calc_maturity <- function(df, df_row) {
  diff <- as.numeric(df[df_row, 'expDate'] - df[df_row, 'Date'])
  return(diff / 252)
}