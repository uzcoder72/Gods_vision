"""
███████ ██████  ██████  ███████ ██   ██ ███████ ██ ████████ ██  ██████  ██ 
██      ██   ██ ██   ██ ██       ██ ██  ██      ██    ██    ██ ██    ██ ██ 
█████   ██████  ██████  █████     ███   █████   ██    ██    ██ ██    ██ ██ 
██      ██   ██ ██   ██ ██       ██ ██  ██      ██    ██    ██ ██    ██ ██ 
██      ██   ██ ██   ██ ███████ ██   ██ ██      ██    ██    ██  ██████  ██ 

==================================================================================
                          GOD'S VISION COMBINATION GENERATOR
==================================================================================

⚠️  ⚠️  ⚠️  IMPORTANT LEGAL AND ETHICAL DISCLAIMER ⚠️  ⚠️  ⚠️

This software is provided for EDUCATIONAL and RESEARCH purposes ONLY.

The creator of this code (github.com/uzcoder72) expressly prohibits and 
does not condone the use of this software for:

❌ ILLEGAL ACTIVITIES including but not limited to:
   - Unauthorized computer access
   - Brute force attacks on systems you don't own
   - Password cracking without explicit permission
   - Any form of cybercrime
   - Harassment or abuse
   - Data theft

❌ UNETHICAL USES including but not limited to:
   - Testing systems without written authorization
   - Security research without proper scope and permission
   - Violating terms of service
   - Privacy invasion

✅ APPROVED USES include:
   - Academic research on combinatorics
   - Password strength analysis on YOUR OWN systems
   - Educational demonstrations
   - Security research with EXPLICIT WRITTEN PERMISSION
   - Testing YOUR OWN systems

BY USING THIS SOFTWARE, YOU AGREE THAT:

1. You will use this tool ONLY for legal and ethical purposes
2. You have proper authorization for any system you test
3. You accept FULL responsibility for your actions
4. The creator is NOT liable for any misuse
5. You comply with all applicable laws in your jurisdiction

VIOLATORS ASSUME ALL LEGAL RESPONSIBILITY AND RISK.

The creator makes no warranties and is not responsible for misuse or damage.
If you cannot agree to these terms, DO NOT USE THIS SOFTWARE.

==================================================================================
"""

import itertools
import string
import time
import sys

def display_warning():
    """Display ethical use warning that must be acknowledged"""
    warning = """
    ⚠️  WARNING: LEGAL AND ETHICAL USE REQUIRED ⚠️
    
    This software generates combinations for EDUCATIONAL purposes ONLY.
    
    ILLEGAL USES INCLUDE:
    • Unauthorized system access
    • Brute force attacks without permission  
    • Password cracking without ownership
    • Any cybercrime activities
    
    By continuing, you CERTIFY that:
    ✓ You will use this tool LEGALLY and ETHICALLY
    ✓ You have proper AUTHORIZATION for any testing
    ✓ You accept FULL RESPONSIBILITY for your actions
    ✓ You understand the CREATOR IS NOT LIABLE for misuse
    
    Type 'I ACCEPT' to continue or anything else to exit: """
    
    response = input(warning)
    if response.strip().upper() != 'I ACCEPT':
        print("❌ Agreement not accepted. Exiting.")
        sys.exit(0)
    print("✅ Agreement accepted. Starting generation...\n")

def generate_ethical_combinations():
    """
    Generate combinations for EDUCATIONAL and AUTHORIZED testing purposes ONLY
    """
    # Character set for educational combinatorics research
    english_letters = string.ascii_letters  # a-zA-Z
    numbers = string.digits  # 0-9
    symbols = '!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{}~'
    
    all_chars = english_letters + numbers + symbols
    charset_size = len(all_chars)
    
    print(f"🔢 Character set size: {charset_size} characters")
    print("📝 Purpose: Academic combinatorics research\n")
    
    # Legal notice in generated file
    legal_header = """# ===========================================================================
# GOD'S VISION COMBINATION GENERATOR - EDUCATIONAL USE ONLY
# ===========================================================================
# 
# LEGAL DISCLAIMER:
# This file contains combinations generated for ACADEMIC RESEARCH and 
# AUTHORIZED SECURITY TESTING only.
#
# MISUSE OF THIS DATA FOR UNAUTHORIZED ACTIVITIES IS STRICTLY PROHIBITED
# AND MAY CONSTITUTE A CRIME.
#
# Users must ensure they have EXPLICIT WRITTEN PERMISSION for any testing.
# Creator is not liable for misuse.
#
# Generated for: Combinatorics Research & Authorized Security Education
# ===========================================================================
#
"""
    
    target_bytes = 50 * 1024 * 1024 * 1024  # 50GB
    batch_size = 50000
    bytes_written = 0
    total_lines = 0
    
    with open('Heavenly_memory.txt', 'w', encoding='utf-8') as f:
        # Write legal header
        f.write(legal_header)
        bytes_written += len(legal_header.encode('utf-8'))
        
        start_time = time.time()
        last_update = start_time
        
        # Generate for educational research purposes
        for length in range(8, 17):
            print(f"\n📊 RESEARCH: Generating length {length} combinations...")
            
            bytes_per_line = length + 2
            remaining_bytes = target_bytes - bytes_written
            max_lines_this_length = remaining_bytes // bytes_per_line
            
            if max_lines_this_length <= 0:
                print("🎯 Research target reached: 50GB data collected")
                break
            
            total_combinations_length = charset_size ** length
            
            if length <= 13:
                lines_to_generate = total_combinations_length
                print(f"   Collecting FULL dataset: {lines_to_generate:,} combinations")
            else:
                lines_to_generate = min(total_combinations_length, max_lines_this_length)
                print(f"   Collecting SAMPLE dataset: {lines_to_generate:,} of {total_combinations_length:,}")
            
            count = 0
            batch = []
            
            generator = itertools.product(all_chars, repeat=length)
            
            for combo in generator:
                if count >= lines_to_generate:
                    break
                    
                combination = ''.join(combo)
                batch.append(combination + '\n')
                count += 1
                total_lines += 1
                
                if len(batch) >= batch_size:
                    f.writelines(batch)
                    bytes_written += sum(len(line) for line in batch)  # FIXED: Removed duplicate 'for line'
                    batch = []
                    
                    current_time = time.time()
                    if current_time - last_update >= 5:
                        elapsed = current_time - start_time
                        lines_per_sec = total_lines / elapsed
                        progress_pct = (count / lines_to_generate) * 100
                        
                        print(f"   📈 Progress: {progress_pct:.1f}% | "
                              f"🚀 Speed: {lines_per_sec:,.0f} lines/sec | "
                              f"💾 Size: {bytes_written/(1024**3):.1f} GB")
                        last_update = current_time
                
                if bytes_written >= target_bytes:
                    break
            
            # Write final batch for this length
            if batch:
                f.writelines(batch)
                bytes_written += sum(len(line) for line in batch)  # FIXED: Removed duplicate 'for line'
            
            print(f"   ✅ Length {length} research complete: {count:,} combinations")
            
            if bytes_written >= target_bytes:
                print("🎯 Research data collection complete: 50GB reached")
                break
    
    end_time = time.time()
    total_time = end_time - start_time
    
    print(f"\n🎉 ACADEMIC RESEARCH COMPLETE 🎉")
    print(f"📊 Total research samples: {total_lines:,}")
    print(f"💾 Final dataset size: {bytes_written/(1024**3):.2f} GB")
    print(f"⏱️  Research duration: {total_time/3600:.2f} hours")
    print(f"📈 Collection rate: {total_lines/total_time:,.0f} samples/second")
    print(f"💡 Legal use reminder: This data is for AUTHORIZED RESEARCH only!")
    print(f"📁 Output: Heavenly_memory.txt")

def main():
    """Main function with comprehensive legal protection"""
    print(__doc__)  # Show the disclaimer header
    
    # Require ethical agreement
    display_warning()
    
    # Show research purpose confirmation
    print("🔬 RESEARCH PURPOSE CONFIRMATION")
    print("This tool will generate combinatorial data for:")
    print("• Academic combinatorics research")
    print("• Authorized security education") 
    print("• Password strength analysis (ONLY on your own systems)")
    print("• Mathematical pattern research\n")
    
    response = input("🔍 Confirm research purpose (type 'RESEARCH' to continue): ")
    if response.strip().upper() != 'RESEARCH':
        print("❌ Research purpose not confirmed. Exiting.")
        return
    
    # Generate for educational purposes
    generate_ethical_combinations()
    
    # Final legal reminder
    print(f"\n{'='*80}")
    print("⚠️  LEGAL REMINDER: This generated data is for AUTHORIZED EDUCATIONAL USE ONLY")
    print("   Misuse for unauthorized activities may constitute criminal offenses.")
    print("   Users assume full responsibility for compliant usage.")
    print(f"{'='*80}")

if __name__ == "__main__":
    main()