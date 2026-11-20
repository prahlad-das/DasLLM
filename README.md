# DasLLM
This is a custom llm hosted on my computer and exposed an API to be used by agent. Later on, this LLM will be used for Agents. 

```
| Process for self hosting |
                                                        |
                                                        ▼
                                        -----------------------------------                                                                                                     
                                       |   Choose an LLM from HuggingFace  |
                                        -----------------------------------                  
                                                        |
                                                        ▼
                                         ----------------------------------
                                        |  Try it locally to see the       |
                                        |  quality of LLM response and.    |
                                        |  change LLM if required          |
                                          ---------------------------------
                                                        |                                                     
                                                        ▼
                                         ---------------------------------------
                                        |  Download Tokenizer and model Tensors |
                                        |  Load model from local repo and test. |
                                         ---------------------------------------
                                                        |
                                                        ▼
                                         --------------------------------------
                                        |  Create POST API, Load model Tensors |
                                        |  in GPU, add inputs to GPU, get      |
                                        |  response and return                 |
                                         --------------------------------------
                                                        |
                                                        ▼
                                          -------------------------------------
                                         |         Secure API with tokens      |
                                          -------------------------------------
                                                         |
                                                         ▼    

                                                                                                                                                       
```
