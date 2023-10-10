load("retriever_lengths.Rda")
load("doodle_lengths.Rda")
```

```{r}
# calculate mean_retriever_l and mean_doodle_l here:
mean_retriever_l <- mean(retriever_lengths)
mean_retriever_l
mean_doodle_l <- mean(doodle_lengths)
mean_doodle_l
```

```{r}
# calculate mean_difference here:
mean_difference <- mean_retriever_l - mean_doodle_l
mean_difference
```

```{r}
# statements:
st_1 <- "The average length of Golden Retrievers is 2.5 inches longer than the average length of Goldendoodles."
st_2 <- "The average length of Golden Retrievers is the same as the average length of Goldendoodles."

# update null_hypo here:
null_hypo <- "st_2"