# Decision Tree Classifier using rpart

library(rpart)
library(rpart.plot)

# Train a classification decision tree
# Inputs: data frame, target column name, complexity parameter, min split size
# Output: trained model
train_decision_tree <- function(data, target_col, cp = 0.01, minsplit = 20) {
  formula <- as.formula(paste(target_col, "~ ."))
  
  model <- rpart(formula, data = data, method = "class",
                 control = rpart.control(cp = cp, minsplit = minsplit))
  return(model)
}

# Visualize the decision tree
plot_tree <- function(model) {
  rpart.plot(model, type = 4, extra = 104, box.palette = "RdBu")
}

# Example: Iris dataset classification
data(iris)
set.seed(42)

# 80/20 train-test split
train_idx <- sample(1:nrow(iris), 0.8 * nrow(iris))
train_data <- iris[train_idx, ]
test_data <- iris[-train_idx, ]

# Train and visualize
tree_model <- train_decision_tree(train_data, "Species", cp = 0.001)
plot_tree(tree_model)

# Predict and evaluate
predictions <- predict(tree_model, test_data, type = "class")
accuracy <- mean(predictions == test_data$Species)
print(paste("Accuracy:", round(accuracy * 100, 2), "%"))

# Tips:
# - Use printcp(model) to find optimal cp for pruning
# - Prune with: prune(model, cp = optimal_cp)
# - For regression: change method to "anova"