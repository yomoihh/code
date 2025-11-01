class LexicalAnalyzer:
    def __init__(self):
        # 定义状态
        self.q0 = 0  # 初始状态
        self.q1 = 1  # 已读1个字符（0或1）
        self.q2 = 2  # 已读2个字符（记录是否出现过0）
        self.q3 = 3  # 已读≥3个字符且出现过0（接受状态）
        self.q4 = 4  # 已读≥3个字符但未出现过0（非法状态）
        
        # 辅助状态变量：记录是否出现过0
        self.has_zero = False
        # 当前字符计数
        self.char_count = 0
        # 当前状态
        self.current_state = self.q0
    
    def reset(self):
        """重置分析器状态"""
        self.current_state = self.q0
        self.has_zero = False
        self.char_count = 0
    
    def transition(self, char):
        """根据输入字符进行状态转换"""
        # 更新字符计数
        self.char_count += 1
        
        # 检查是否出现0
        if char == '0':
            self.has_zero = True
        
        # 状态转换逻辑
        if self.current_state == self.q0:
            # 第一个字符
            self.current_state = self.q1
                
        elif self.current_state == self.q1:
            # 第二个字符
            self.current_state = self.q2
                
        elif self.current_state == self.q2:
            # 第三个字符
            if self.has_zero:
                self.current_state = self.q3  # 有0，进入接受状态
            else:
                self.current_state = self.q4  # 无0，进入非法状态
                
        elif self.current_state == self.q3:
            # 已在接受状态（≥3个字符且有0），保持状态
            self.current_state = self.q3
                
        elif self.current_state == self.q4:
            # 已在非法状态（≥3个字符但无0）
            if self.has_zero:
                self.current_state = self.q3  # 如果现在出现0，转为接受状态
            else:
                self.current_state = self.q4  # 仍无0，保持非法状态
                
        return True
    
    def analyze(self, input_string):
        """分析输入的字符串"""
        self.reset()
        
        # 检查输入是否只包含0和1
        for char in input_string:
            if char not in ['0', '1']:
                return False, f"错误：输入包含非法字符'{char}'，只能包含'0'和'1'"
        
        # 逐个字符处理
        for char in input_string:
            self.transition(char)
        
        # 检查最终状态和条件
        if self.current_state == self.q3:
            return True, "合法字符串（长度>2且至少包含一个0）"
        elif self.char_count <= 2:
            return False, f"错误：字符串长度不足（当前长度{self.char_count}，需要>2）"
        elif self.current_state == self.q4:
            return False, "错误：字符串中不包含'0'"
        else:
            return False, "未知错误"

# 测试程序
def test_analyzer():
    analyzer = LexicalAnalyzer()
    
    # 测试用例
    test_cases = [
        "000",     # 合法（长度3，有0）
        "001",     # 合法
        "010",     # 合法
        "100",     # 合法
        "101",     # 合法
        "110",     # 合法
        "01",      # 非法（长度不足）
        "11",      # 非法（长度不足且无0）
        "0",       # 非法（长度不足）
        "1",       # 非法（长度不足且无0）
        "111",     # 非法（无0）
        "1111",    # 非法（无0）
        "1110",    # 合法（长度4，有0）
        "0111",    # 合法
        "1011",    # 合法
        "0a1",     # 非法（含非法字符）
        "",        # 非法（空字符串）
    ]
    
    print("字符串分析结果：")
    print("-" * 60)
    for test_str in test_cases:
        is_valid, message = analyzer.analyze(test_str)
        status = "✓" if is_valid else "✗"
        print(f"{status} '{test_str}': {message}")

# 交互式测试
def interactive_test():
    analyzer = LexicalAnalyzer()
    
    print("01字符串词法分析器")
    print("规则：必须至少包含1个'0'且长度必须大于2（即至少3个字符）")
    print("输入'quit'退出程序")
    print("-" * 60)
    
    while True:
        input_str = input("请输入字符串: ").strip()
        
        if input_str.lower() == 'quit':
            break
            
        is_valid, message = analyzer.analyze(input_str)
        status = "合法" if is_valid else "非法"
        print(f"结果: {status} - {message}")
        print()

if __name__ == "__main__":
    # 运行测试用例
    test_analyzer()
    print("\n" + "="*60 + "\n")
    
  



