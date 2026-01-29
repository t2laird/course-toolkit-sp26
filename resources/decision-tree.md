Decision Tree in R (rpart)
Link: https://cran.r-project.org/web/packages/rpart/index.html
Description:
    A template and package for making classification and regression trees in R. The rpart package provides a flexible framework for building decision trees to model categorical or continuous outcomes.
Why it's useful:
    Use this when you need interpretable models for prediction or classification tasks. Decision trees are great for understanding feature importance, handling non-linear relationships without transformations, and creating visualizations that non-technical stakeholders can understand. Common applications include customer churn prediction, medical diagnosis, and credit risk assessment.
Example/Notes:
    Install with install.packages("rpart") and install.packages("rpart.plot") for visualization
    Basic syntax: model <- rpart(target ~ ., data = train_data, method = "class") for classification
    Use rpart.plot(model) for clean tree visualizations
    Prune trees with prune(model, cp = optimal_cp) to prevent overfitting
    Consider setting minsplit and maxdepth parameters to control tree complexity