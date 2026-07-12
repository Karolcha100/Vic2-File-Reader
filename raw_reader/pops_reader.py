



class Reader:
    def __init__(
            self, 
            verbose: bool = False,
        ) -> None:
        self.verbose: bool = verbose
    
    @staticmethod
    def locally_check_index_in_text(text: str, char_moved: int) -> bool:
        return char_moved >= 0 and char_moved < len(text)
    
    @staticmethod
    def move_forward_until_on(text: str, stopping_symbols: set[str]) -> int:
        char_moved: int = 0

        while(char_moved < len(text) and text[char_moved] not in stopping_symbols):
            char_moved += 1

        return char_moved
    
    @staticmethod
    def move_forward_only_on(text: str, NOT_stopping_symbols: set[str]) -> int:
        char_moved: int = 0
        
        while(char_moved < len(text) and text[char_moved] in NOT_stopping_symbols):
            char_moved += 1

        return char_moved
    
    @staticmethod
    def move_forward_on_signs_in_order(text: str, ordered_signs: list[set[str]]) -> int:
        char_moved: int = 0

        for step_signs in ordered_signs:
            char_moved += Reader.move_forward_until_on(text[char_moved:], step_signs)

        if Reader.locally_check_index_in_text(text, char_moved):
            return char_moved
        else:
            return len(text)-1
        
    @staticmethod
    def move_forward_one_word(text: str) -> int:
        return Reader.move_forward_until_on(text, {'\n', '\t', ' ', '\r', '#', '{'})
    
    @staticmethod
    def check_if_list(text: str) -> bool:
        return Reader.move_forward_until_on(text, {'='}) > Reader.move_forward_until_on(text, {'}'})
    
    @staticmethod
    def read_list(text: str) -> tuple[int, str]:
        # TODO: Checking if opening on {
        char_end_of_list: int = Reader.move_forward_until_on(text, {'}'})
        readed_list = text[1:char_end_of_list].strip()

        return (char_end_of_list, readed_list)

    @staticmethod
    def read_sentence_with_equal_sign(text: str) -> tuple[int, str, str]:
        char_moved: int = 0
        first_word: str = ''
        char_tmp: int = 0
        second_word: str = ''


        char_moved += Reader.move_forward_one_word(text[char_moved:])

        first_word = text[:char_moved]


        char_tmp = char_moved + Reader.move_forward_only_on(text[char_moved:], {'\n', '\t', ' ', '\r', '='})
        char_moved = char_tmp + Reader.move_forward_one_word(text[char_tmp:])

        second_word = text[char_tmp:char_moved]

        return (char_moved, first_word, second_word)
    
    @staticmethod
    def move_ignore_whole_bracket(text: str) -> int:
        if text[0] not in {'{'}:
            raise ValueError(f"[{'ignore_whole_bracket'}] Cannot ignore something which is not starting on bracket!!!")
        
        bracket_deep_counter: int = 1
        char_moved = 0

        while(bracket_deep_counter > 0):
            char_moved += 1

            if char_moved >= len(text):
                raise ValueError(f"[{'ignore_whole_bracket'}] Cannot find end bracket in given text!!!") 

            if text[char_moved] in {'{'}:
                bracket_deep_counter += 1
            elif text[char_moved] in {'}'}:
                bracket_deep_counter -= 1
            else:
                pass

        return char_moved
    
    @staticmethod
    def move_skip_hashtag(text) -> int:
        char_moved: int = 0

        if text[char_moved] not in {'#'}:
            raise ValueError(f"[{'skip hashtag'}] Cannot skip something which is not hashtag!!!")
        
        return Reader.move_forward_until_on(text[char_moved:], {'\n'})
        
    @staticmethod
    def enter_bracket(text: str) -> tuple[int, dict[str, str]]:
        if text[0] not in {'{'}:
            raise ValueError(f"[{'enter_bracket'}] Cannot enter something which is not starting on bracket!!!")
        
        char_moved: int = 0
        char_tmp: int
        return_stats: dict[str, str] = {}
        tmp_stats: dict[str, str]
        tmp_str_key: str = ''
        tmp_str_value: str

        char_moved += 1

        while(text[char_moved] not in {'}'}):            

            if text[char_moved] in {'#'}:
                char_moved += Reader.move_skip_hashtag(text[char_moved:])
                continue

            elif text[char_moved] in {'='}:
                raise NotImplementedError(f"[{'enter_bracket'}] Entered SPECIFIED [{text[char_moved]}] sign!!!")
                continue

            elif text[char_moved] in {'{'}:
                if Reader.check_if_list(text[char_moved:]):
                    char_tmp, tmp_str_value = Reader.read_list(text[char_moved:])
                    return_stats[f"{tmp_str_key}"] = tmp_str_value
                else:
                    char_tmp, tmp_stats = Reader.enter_bracket(text[char_moved:])
                    return_stats.update({f"{tmp_str_key}-{tmp_key}": tmp_val for tmp_key, tmp_val in tmp_stats.items()})
                char_moved += char_tmp + 1
                continue

            elif text[char_moved] in {'\n', '\t', ' ', '\r'}:
                char_moved += Reader.move_forward_only_on(text[char_moved:], {'\n', '\t', ' ', '\r'})
                continue

            elif text[char_moved] not in {'\n', '\t', ' ', '\r', '{', '}', '=', '#'}:
                char_tmp, tmp_str_key, tmp_str_value = Reader.read_sentence_with_equal_sign(text[char_moved:])

                if len(tmp_str_value) == 0:
                    pass
                else:
                    return_stats[tmp_str_key] = tmp_str_value

                char_moved += char_tmp

                continue

            else:
                raise NotImplementedError(f"[{'enter_bracket'}] Entered UNKNOWN [{text[char_moved]}] sign!!!")
            
        if char_moved >= len(text):
            raise ValueError(f"[{'enter_bracket'}] Exited The Text!!!")
                  
        return (char_moved, return_stats)




    
    def translate_text(self, text: str) -> dict[str, str]:
        char_index: int = 0
        char_tmp_index: int
        return_stats: dict[str, str] = {}
        tmp_stats: dict[str, str]

        # TODO: Version reading multiple units in one file
        char_index += Reader.move_forward_until_on(text[char_index:], {'{'})

        char_tmp_index, tmp_stats = self.enter_bracket(text[char_index:])

        char_index += char_tmp_index + 1
        return_stats.update(tmp_stats)

        return return_stats


        


        