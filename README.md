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
(Download and put model in LLM/Model repo according to download_model.py and install requirements.txt, model not included in git due to size)
Latency observed: 1m to 4m
