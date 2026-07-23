plt.figure(figsize=(10, 5))

sns.heatmap(
    df[[
        "study_hours",
        "attendance_percentage",
        "math_score",
        "science_score",
        "english_score",
        "overall_score"
    ]].corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.show()