# Metadata: Cost

## How much does it cost...

- to purchase a Stata/MP-32 license?
- to obtain access for three years to Compustat for China?
- to travel to Norway for in-person access to linked employer-employee data?
- to run a computation with 20,000 core-hours, using `x2iedn.32xlarge` (128 CPUs with 4TB of memory)?

## How much does it cost...

- Stata/MP-32: **\$3,295** (2 users)
- Compustat for China? **\$500,000**
- 3 weeks Norway: **\$3,000**
- 20,000 core-hours/ `x2iedn.32xlarge`: **\$4168.125**

## Again...


{{< include robot.include >}}


## How much does it cost...

- To `train` your model in the cloud?
- To run the model on your data *once*?
- To run the model **multiple times** to assess variability?

## When it costs A LOT

-    provide a subsample of your data that can be cheaper/faster to reproduce
- use that subsample to look at robustness yourself 
  - how does it change when you use different models,
  - how does it change when, just before submitting the package, you run it through again on the same model (or what you think is the same model).

## Does it need to cost a lot?

run it through on the "best" open source model, and compare the output. 

- Is it robust (again)? 
- Is it "better"/"worse" (and what metric did you choose)? 