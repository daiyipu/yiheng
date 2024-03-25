
def __illegal_json_ends(s):
    temp_json = s
    illegal_json_ends_1 = [", }", ",}"]
    illegal_json_ends_2 = ", ]", ",]"
    for illegal_json_end in illegal_json_ends_1:
        temp_json = temp_json.replace(illegal_json_end, " }")
    for illegal_json_end in illegal_json_ends_2:
        temp_json = temp_json.replace(illegal_json_end, " ]")
    return temp_json    

def __json_interception(s, is_json_array: bool = False):
    try:
        if is_json_array:
            i = s.find("[")
            if i < 0:
                return ""
            count = 1
            for j, c in enumerate(s[i + 1 :], start=i + 1):
                if c == "]":
                    count -= 1
                elif c == "[":
                    count += 1
                if count == 0:
                    break
                assert count == 0
                return s[i : j + 1]
        else:
            i = s.find("{")
            if i < 0:
                return ""
            count = 1
            for j, c in enumerate(s[i + 1 :], start=i + 1):
                if c == "}":
                    count -= 1
                elif c == "{":
                    count += 1
                if count == 0:
                    break
            assert count == 0
            return s[i : j + 1]
    except Exception as e:
        return ""    

def __extract_json(s):
    try:
        # Get the dual-mode analysis first and get the maximum result
        temp_json_simple = __json_interception(s)
        temp_json_array = __json_interception(s, True)
        if len(temp_json_simple) > len(temp_json_array):
            temp_json = temp_json_simple
        else:
            temp_json = temp_json_array

        if not temp_json:
            temp_json = __json_interception(s)

        temp_json = __illegal_json_ends(temp_json)
        return temp_json
    except Exception as e:
        raise ValueError("Failed to find a valid json in LLM response！" + temp_json)


def __illegal_json_ends(s):
    temp_json = s
    illegal_json_ends_1 = [", }", ",}"]
    illegal_json_ends_2 = ", ]", ",]"
    for illegal_json_end in illegal_json_ends_1:
        temp_json = temp_json.replace(illegal_json_end, " }")
    for illegal_json_end in illegal_json_ends_2:
        temp_json = temp_json.replace(illegal_json_end, " ]")
    return temp_json

def parse_prompt_response(model_out_text):
    cleaned_output = model_out_text.rstrip()
    if "```json" in cleaned_output:
         _, cleaned_output = cleaned_output.split("```json")
    if cleaned_output.startswith("```json"):
        cleaned_output = cleaned_output[len("```json") :]
    if cleaned_output.startswith("```"):
        cleaned_output = cleaned_output[len("```") :]
    if cleaned_output.endswith("```"):
        cleaned_output = cleaned_output[: -len("```")]
    cleaned_output = cleaned_output.strip()
    if not cleaned_output.startswith("{") or not cleaned_output.endswith("}"):
        cleaned_output = __extract_json(cleaned_output)
    cleaned_output = (
        cleaned_output.strip()
        .replace("\\n", " ")
        .replace("\n", " ")
        .replace("\\", " ")
    )
    cleaned_output = __illegal_json_ends(cleaned_output)
    return cleaned_output

# class DbChatOutputParser(BaseOutputParser):
# def parse_prompt_response(self, model_out_text):
# 方法写的有问题
if __name__ == '__main__':
    model_out_text = "根据您提供的信息，公司业务表的结构如下： ```sql CREATE TABLE `company_business` (   `id` int(11) NOT NULL AUTO_INCREMENT,   `company_id` varchar(64) DEFAULT NULL COMMENT '企业ID',   `business_type` varchar(128) DEFAULT NULL COMMENT '业务类型',   `start_date` datetime DEFAULT NULL COMMENT '开始日期',   `end_date` datetime DEFAULT NULL COMMENT '结束日期',   PRIMARY KEY (`id`),   KEY `i_company_id` (`company_id`) USING BTREE ) ENGINE=InnoDB AUTO_INCREMENT=1039 DEFAULT CHARSET=utf8 COMMENT='公司业务表' ``` 请注意，该表中包含以下列：  - `id`：自增长的主键列，用于唯一标识每个记录。 - `company_id`：企业ID，用于关联到公司的其他记录。 - `business_type`：业务类型，用于指定业务类型。 - `start_date`：开始日期，用于记录业务开始的时间。 - `end_date`：结束日期，用于记录业务结束的时间。"
    clean_str = parse_prompt_response(model_out_text)
    print("clean prompt response:",clean_str)




